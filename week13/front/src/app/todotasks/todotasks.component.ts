import { Component, OnInit } from '@angular/core';
import { ITaskList, ITask } from "../shared/models/models";
import { ActivatedRoute } from '@angular/router';
import { ProviderService } from "../shared/services/provider.service";

@Component({
  selector: 'app-todotasks',
  templateUrl: './todotasks.component.html',
  styleUrls: ['./todotasks.component.css']
})
export class TodotasksComponent implements OnInit {
public tasks: ITask[] = [];
public taskList: any = {};
private id:number = 0;
public current_task: ITask;
public mode: String='';
public task_name: any = '';
public status: any = '';
public created_at: any = '';
public due_on: any = '';
  constructor(
    private provider: ProviderService,
    private route: ActivatedRoute) { }

  ngOnInit() {
    this.id = parseInt(this.route.snapshot.paramMap.get('id'))

if (this.id) {
  this.getTasks(this.id)
  }
}
getTasks(id: number){
        this.provider.getTasks(id).then(res => {
          this.tasks = res;
        })
      }


createTask(id: number){
    this.provider.createTask(id, this.task_name, this.created_at, this.due_on, this.status).then(res => {
      this.tasks.push(res);
      this.task_name = '';
      this.created_at = '';
      this.due_on = '';
      this.status = ''
    })
    this.getTasks(this.id);
}

getTask(task: ITask){
  this.updateMode('detail');
  this.provider.getTask(task).then( res => {
    this.current_task = res;
  })
}

updateTask(task: ITask){
  this.provider.updateTask(task).then(res => {
    this.task_name = '';
    this.created_at = '';
    this.due_on = '';
    this.status = '';
    this.getTasks(this.id);
    this.updateMode('detail');
  })
}
updateMode(mode: String){
  this.mode= mode;
}

deleteTask(task: ITask) {
  this.updateMode('delete');
  this.provider.deleteTask(task).then(res => {
    this.provider.getTasks(this.id).then(r => {
      this.tasks = r;
    });
  });
}
}
