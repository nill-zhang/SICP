def country(county_name):
    print("country is called")

    def state(state_name):
        print("state is called")

        def city(city_name):
            print("city is called")

            def district(district_name):
                print("city is called")

                def community(community_name):
                    print("community is called")
                    print(":".join([county_name,
                                    state_name,
                                    city_name,
                                    district_name,
                                    community_name]))
                return community
            return district
        return city
    return state


country_n = "China"
state_n = "AnHui"
city_n = "HeFei"
district_n = "ShuShan"
community_n = "YaoGang"


def scope_test():
    state_func = country(country_n)
    city_func = state_func(state_n)
    district_func = city_func(city_n)
    community_func = district_func(district_n)
    community_func(community_n)
    print("#"*80)
    country(country_n)(state_n)(city_n)(district_n)(community_n)

if __name__ == "__main__":
    scope_test()


