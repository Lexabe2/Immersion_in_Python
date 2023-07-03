# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии


def task_2(names: list[str], bets: list[int], bonus: list[str]) -> dict[
                                                                   str:int]:
    return {name: bet / 100 * float(bon) for name, bet, bon in
            zip(names, bets, map(lambda x: x.replace('%', ''), bonus))}
