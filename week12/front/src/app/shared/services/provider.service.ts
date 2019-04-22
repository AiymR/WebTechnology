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

  createTaskList(name: any): Promise<ITaskList> {
    return this.post('http://localhost:8000/api/task_list/', {
      name: name
    });
  }

  updateTaskList(tasklistname:ITaskList){
    return this.put(`http://localhost:8000/api/task_list/${tasklistname.id}/`,{
      name: tasklistname.name
    });
  }
  deleteTaskList(id:number): Promise<any> {
    return this.delet(`http://localhost:8000/api/task_list/${id}/`,{

    });
  }

  getTask(tasks: ITask): Promise<ITask>{
    return this.get(`http://localhost:8000/api/tasks/${tasks.id}/`, {})
  }
  updateTask(task: ITask) {
    return this.put( `http://localhost:8000/api/tasks/${task.id}/`, {
      name: task.name
    });
  }

  deleteTask(task: ITask) {
    return this.delet(`http://localhost:8000/api/tasks/${task.id}/`, {});
  }

  createTask(tasklist:ITaskList, name: any, created_at: any, due_on: any, status: any): Promise<ITask>{
   return this.post(`http://localhost:8000/api/task_list/${tasklist.id}/task/`, {
     name: name,
     created_at: created_at,
     due_on: due_on,
     status: status
   })
 }

}
