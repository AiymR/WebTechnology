import { Component, OnInit } from '@angular/core';
import { ProviderService } from "../shared/services/provider.service";
import { ITaskList, ITask } from "../shared/models/models";

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public taskLists :ITaskList[]=[];
  public tasks: ITask[] = [];
  public current_list: ITaskList;
  public current_task: ITask;
  public name: any = "";
  public task_name: any='';
  public mode:String='';
 public updateMode = false;

public task_name: any='';
public task_created_at: any='';
public task_due_on: any='';
public task_status: any='';


  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
    });
}

  getIni(){
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
    });
  }


getTasks(taskLists: ITaskList){
      this.provider.getTasks(taskLists).then(res => {
        this.tasks = res;
        this.current_list = taskLists;
      })
    }

getTask(tasks: ITask){
      this.provider.getTask(tasks).then( res => {
      this.current_task = res;
        })
      }
createTaskList() {
          if (this.name !== "") {
            this.provider.createTaskList(this.name).then(res => {
              this.taskLists.push(res);
              this.name = "";
              this.provider.getTaskLists().then(r => {
                this.taskLists = r;
              });
            });
          }
        }


updateTaskList(taskList: ITaskList) {
    this.updateMode = true;
    this.provider.updateTaskList(taskList).then(res => {});
  }

deleteTaskList(c: ITaskList) {
    this.provider.deleteTaskList(c.id).then(res => {
      this.provider.getTaskLists().then(r => {
        this.taskLists = r;
      });
    });
  }

  updateTask(task: ITask) {

    this.provider.updateTask(task).then(res => {
    });
  }

   deleteTask(task: ITask) {
    this.provider.deleteTask(task).then(res => {
      this.provider.getTasks(taskLists).then(r => {
        this.tasks = r;
        this.current_list = taskLists;
      });
    });
  }

createTask(task_list: ITaskList){
    this.provider.createTask(task_list, this.task_name, this.task_created_at, this.task_due_on, this.task_status).then(res => {
      this.tasks.push(res);
      this.task_list_name = '';
      this.task_created_at = '';
      this.task_due_on = '';
      this.task_status = ''
    })

}


}
