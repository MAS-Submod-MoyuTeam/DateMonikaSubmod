# TODO: Translation updated at 2022-08-31 07:16

# game/Submods/DateMonikaSubmod/Date_Submod.rpy:26
translate chinese pick_date_7535efb9:

    # m 1sublb "We're going on a date?"
    m 1sublb "我们要去约会吗？"

# game/Submods/DateMonikaSubmod/Date_Submod.rpy:27
translate chinese pick_date_a565e9c1:

    # m 3hub "Sounds exciting~!"
    m 3hub "听起来很刺激 ~ ！"

# game/Submods/DateMonikaSubmod/Date_Submod.rpy:28
translate chinese pick_date_a69647a4:

    # m 1eua "Where do you want to go for our date?{nw}"
    m 1eua "你想去哪里开始我们的约会呢? {nw}"

# game/Submods/DateMonikaSubmod/Date_Submod.rpy:31
translate chinese pick_date_102b110e:

    # m "Where do you want to go for our date?{fast}" nointeract
    m "你想去哪里开始我们的约会呢?{fast} " nointeract

# game/Submods/DateMonikaSubmod/Date_Submod.rpy:49
translate chinese pick_date_bd2a5f73:

    # m 1eka "Oh, alright."
    m 1eka "哦, 好吧。"

translate chinese strings:
    
    old "Error: Script file is missing or corrupt.\nPlease check or reinstall the Submod."
    new "错误：脚本文件丢失或损坏.\n请检查并重新安装子模组"
    
    # game/Submods/DateMonikaSubmod/Date_Submod.rpy:30
    old "Cafe"
    new "咖啡馆"

    # game/Submods/DateMonikaSubmod/Date_Submod.rpy:30
    old "Park"
    new "公园"

    # game/Submods/DateMonikaSubmod/Date_Submod.rpy:30
    old "Beach"
    new "湖滨"

translate chinese python:
    addEvent(Event(persistent.event_database,eventlabel="pick_date",category=['约会'],prompt="让我们开始一个约会吧~",pool=True,unlocked=True))
