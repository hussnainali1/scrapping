

def main():
    from admission_news_eduvision.admission import admission
    from jobs.temp_job import jobsClass

    # ==================== admissions
    link_bs_admissions = "https://www.eduvision.edu.pk/admissions.php?discipline_type=&sub_level=7&city=&pageNo=1"
    link_ms_admissons = "https://www.eduvision.edu.pk/admissions.php?discipline_type=&sub_level=3&city=&pageNo=1"
    # ====================

    # ============
    jobs_com = "https://jobs.com.pk/find/"

    # #==================== DAWN NEWS

    # ===========

    # ==================== Admissions ================
    print("BS Admissions")
    temp = admission(link_bs_admissions, "BS")
    temp.mainProMethod()

    print("MS admissions")
    temp = admission(link_ms_admissons, "MS")
    temp.mainProMethod()

    # ==================== JOBS NEWS
    print("Jobs News")
    temp = jobsClass(jobs_com, "Jobs")
    temp.mainPro()


if __name__ == '__main__':
    main()
# D:\project\proj\newsBuzz\server\dataFiles
