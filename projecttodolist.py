class Task:
    def __init__(self,title,due_date,category):
          self.title = title
          self.due_date = due_date
          self.category = category
          self.is_complate = False
          
    def mark_as_complated(self):
        self.is_complate = True
        
    def __str__(self):
        status = "selesai" if self.is_complate else "belum selesai"
        return f"judul: {self.title},batas waktu{self.due_date},kategori{self.category},status{status}"
    
class todolist:
    def __init__(self):
        self.task = []
        
    def add_task(self,task):
        self.task.append(task)
        print(f'tugas"{task.title}"berhasil ditambahkan.')
        
    def remove_task(self,title):
        for task in self.task:
            if task.title == title:
               self.task.remove(task)
               print(f'tugas"{title}"berhasil dihapus.')
               return
        print (f'tugas dengan judul"{title}"tidak ditemukan.')
        
    def mark_as_complate(self,title):
        for task in self.task:
            task.mark_as_complate()
            print(f'tugas"{title}"ditandai sebagai selesai.')
            return
        print(f'tugas dengan judul"{title}"tidak ditemukan.')
        
    def display_task(self,filter_category=None):
        if not self.task:
            print("tidak ada yang tersedia.")
        else:
            for task in self.task:
                if filter_category is None or task.category == filter_category:
                    print(task)
                    
                    
        def add_task_manually(todo_list):
            title = input("masukan judul tugas: ")
            due_date = input("masukan batas waktu tugas(yyyy-mm-dd): ")
            category = input("masukan kategori tugas: ")
            
            task = task(title,due_date,category)
            todo_list.add_task(task)
            
            
#membuat todo_list
todo_list = ToDolist()

while true:
    print("/nMenu:")
    print("1.tambah tugas")
    print("2.tampilkan semua tugas")
    print("3.tampilkan tugas berdasarkan kategori")
    print("4.tadai tugas sebagai selesai")
    print("5.hapus tugas")
    print("6.keluar")                        
                    
                    
                        
                        
                        
            
                                  