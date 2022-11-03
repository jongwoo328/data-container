from container import Container


def main():
    container = Container()

    for i in range(300):
        # 0 ~ 299 까지 숫자를 추가
        container.add(i)

        if (i + 1) % 10 == 0:
            # 데이터 수 체크 : len(container)
            print(f"loop : {i + 1}", f"container : {container}", f"data 수 : {len(container)}")

    # 데이터 가져오기 (list로)
    data = container.get_data()

    # 100 ~ 299 까지 저장되는 것을 확인 가능
    print(data)


if __name__ == "__main__":
    main()
