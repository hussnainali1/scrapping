

def main():
    from dawn.world_category import world
    from dawn.tech_dawn import tech
    from dawn.whole_sports_category_dawn import sports

    dawn_tech_link = "https://www.dawn.com/tech"
    dawn_world_link = "https://www.dawn.com/world"
    dawn_sports_link = "https://www.dawn.com/sport"
    # ============

    # # #==================== DAWN NEWS
    print("DAWN SPORTS")
    temp = sports(dawn_sports_link, "sports")
    temp.mainMethod1()
    print("DAWN TECHOLOGY")
    temp = tech(dawn_tech_link, "technology")
    temp.mainMethod1()
    print("DAWN WORLD NEWS")
    temp = world(dawn_world_link, "worlds")
    temp.mainMethod()

    # #============

    # #==================== Admissions ================


if __name__ == '__main__':
    main()
# D:\project\proj\newsBuzz\server\dataFiles
