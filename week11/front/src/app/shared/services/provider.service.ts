import { Injectable, EventEmitter } from '@angular/core';
import {MainService} from "./main.service";
import {HttpClient} from "@angular/common/http";
import {ITaskList, ITask} from "../models/models";

@Injectable({
  providedIn: 'root'
})

export class ProviderService extends MainService{
  public sendMessage = new EventEmitter<string>();

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<ITaskList[]>{
    return this.get('http://localhost:8000/api/task_list/', {});
  }

  getTasks(taskLists: ITaskList): Promise<ITask[]>{
    return this.get(`http://localhost:8000/api/task_list/${taskLists.id}/task`, {})
  }

  getTask(tasks: ITask): Promise<ITask>{
    return this.get(`http://localhost:8000/api/tasks/${tasks.id}/`, {})
  }
}
