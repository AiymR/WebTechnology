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

  constructor(private provider: ProviderService) { }

  ngOnInit() {
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
}
