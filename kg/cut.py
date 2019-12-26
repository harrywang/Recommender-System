from Recommender_System.data.data_loader import ml20m

if __name__ == '__main__':
    data = ml20m()
    item_set = {d[1] for d in data}
    delete_item_list = []
    lines = []

    with open('kg_ml20m&KGCN/item_id2entity_id_old.txt', 'r') as reader:
        for line in reader.readlines():
            item_id = int(line.strip().split('\t')[0])
            if item_id in item_set:
                lines.append(line)
            else:
                delete_item_list.append(item_id)

    with open('kg_ml20m&KGCN/item_id2entity_id.txt', 'w', encoding='utf-8') as writer:
        writer.writelines(lines)

    print(len(delete_item_list))
    print(delete_item_list)
