from phgeograpy.data import philippines


def regions(slug=None, raw=False):
    """
    Usage:
        1. regions() - Returns a list of regions.
        2. regions(<slug>) - Returns a specific region.
    """
    # Return a specific region
    if slug:
        region = philippines['regions'].get(slug)
        if not region:
            raise Exception
        if raw:
            return region
        return Region(
            slug=slug,
            name=region['name'],
            description=region['description'],
        )

    # Return all region
    regions = []
    for slug, region in philippines['regions'].items():
        if raw:
            regions.append(region)
        else:
            regions.append(Region(
                slug=slug,
                name=region['name'],
                description=region['description'],
            ))
    return regions


def provinces(slug=None, region_slug=None, raw=False):
    """
    Usage:
        1. provinces() - Returns a list of provinces all over the Philippines.
        2. provinces(region_slug=<region_slug>) - Returns a list of provinces of a specific region.
        3. provinces(slug=<slug>) - Get a province instance.
        4. provinces(slug=<slug>, region_slug=<region_slug>) - Get a province instance
            from a specific region.
    """
    if slug or region_slug:
        if slug and region_slug:
            # Return a specific province from the given region
            region = regions(region_slug, raw=True)
            province = region['provinces'].get(slug)
            if not province:
                raise Exception
            if raw:
                return province
            return _raw_province_to_model(province, region)
        elif slug:
            # Return a specific province
            for _region_slug, region in philippines['regions'].items():
                province = region['provinces'].get(slug)
                if province:
                    if raw:
                        return province
                    return _raw_province_to_model(slug, province, _region_slug, region)
            raise Exception
        elif region_slug:
            # Return provinces of the given region
            region = regions(region_slug, raw=True)
            return _get_provinces_from_region(region, raw=raw)
        else:
            raise Exception('Unimplemented usage.')

    # Return all province
    provinces = []
    for _region_slug, region in philippines['regions'].items():
        provinces += _get_provinces_from_region(region, raw=raw)
    return provinces


def municipalities(slug=None, province_slug=None, region_slug=None, raw=False):
    """
    Usage:
        1. municipalities() - Returns a list of municipalities all over the Philippines.
        2. municipalities(province_slug=<province_slug>, region_slug=<region_slug>) - Returns a list of municipalities
            from a specific province and region.
        3. municipalities(<slug>, province_slug=<province_slug>, region_slug=<region_slug>) - Get a municipality instance.
    """
    if slug or province_slug or region_slug:
        if slug and province_slug and region_slug:
            # Return a municipality instance
            region = regions(region_slug, raw=True)
            province = provinces(province_slug, region_slug=region_slug, raw=True)
            municipality = province['municipalities'].get(slug)
            if not municipality:
                raise Exception
            if raw:
                return municipality
            return Municipality(
                slug=slug,
                name=municipality['name'],
                is_city=bool(municipality.get('is_city')),
                is_capital=bool(municipality.get('is_capital')),
                is_huc=bool(municipality.get('is_huc')),
                province=_raw_province_to_model(province, region),
            )
        elif not slug and province_slug and region_slug:
            # Return all municipalities from a specific province and region
            region = regions(region_slug, raw=True)
            province = provinces(province_slug, region_slug=region_slug, raw=True)
            return _get_municipalities_from_province(province, region, raw=raw)
        else:
            raise Exception('Unimplemented usage.')

    # Return all municipalities
    municipalities = []
    for slug, region in philippines['regions'].items():
        for slug, province in region['provinces'].items():
            municipalities += _get_municipalities_from_province(province, region, raw=raw)
    return municipalities


"""Raw data utilities"""


def _get_provinces_from_region(region, raw=False):
    provinces = []
    for _province_slug, province in region['provinces'].items():
        if raw:
            provinces.append(province)
        else:
            province = _raw_province_to_model(province, region)
            provinces.append(province)
    return provinces


def _raw_province_to_model(province, region):
    return Province(
        slug=province['slug'],
        name=province['name'],
        region=Region(
            slug=region['slug'],
            name=region['name'],
            description=region['description'],
        ),
    )


def _get_municipalities_from_province(province, region, raw=False):
    municipalities = []
    for slug, municipality in province['municipalities'].items():
        if raw:
            municipalities.append(municipality)
        else:
            municipalities.append(Municipality(
                slug=slug,
                name=municipality['name'],
                is_city=bool(municipality.get('is_city')),
                is_capital=bool(municipality.get('is_capital')),
                is_huc=bool(municipality.get('is_huc')),
                province=_raw_province_to_model(province, region),
            ))
    return municipalities


"""Models"""


class Region:
    """
    An object representation of a region.
    """

    def __init__(self, slug, name, description=None):
        self.slug = slug
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Region(slug={}, name={})>'.format(self.slug, self.name)

    def provinces(self, slug=None):
        return provinces(slug=slug, region_slug=self.slug)


class Province:
    """
    An object representation of a province.
    """

    def __init__(self, slug, name, region):
        self.slug = slug
        self.name = name
        self.region = region

    def __repr__(self):
        return '<Province(slug={}, name={}>'.format(self.slug, self.name)

    def municipalities(self):
        return municipalities(province_slug=self.slug, region_slug=self.region.slug)


class Municipality:
    """
    An object representation of a municipality.
    """

    def __init__(self, slug, name, province, is_city=False, is_capital=False, is_huc=False):
        self.slug = slug
        self.name = name
        self.province = province
        self.is_city = is_city
        self.is_capital = is_capital
        self.is_huc = is_huc

    def __repr__(self):
        return '<Municipality(slug={}, name={}, is_city={})>'.format(self.slug, self.name, self.is_city)

    def baranggays(self):
        raise Exception('Unimplemented method')
