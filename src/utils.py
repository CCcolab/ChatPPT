from pptx import Presentation

def remove_all_slides(prs: Presentation):
    """
    移除演示文稿中的所有幻灯片，并清理相关资源。
    """
    # 获取所有幻灯片的 ID 列表
    slides = list(prs.slides._sldIdLst)

    # 遍历并移除每个幻灯片
    for slide in slides:
        rId = slide.rId  # 获取幻灯片的关联资源 ID
        prs.part.drop_rel(rId)  # 删除关联资源
        prs.slides._sldIdLst.remove(slide)  # 从幻灯片列表中移除

    print("所有默认幻灯片已被移除。")