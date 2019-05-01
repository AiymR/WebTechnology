import { Injectable, EventEmitter } from '@angular/core';
import {MainService} from "./main.service";
import {HttpClient} from "@angular/common/http";
import {ITaskList, ITask, IAuthResponse} from "../models/models";

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

  getTasks(id: number): Promise<ITask[]>{
    return this.get(`http://localhost:8000/api/task_list/${id}/task/`, {})
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

  updateTask(task: ITask){
  return this.put(`http://localhost:8000/api/tasks/${task.id}/`, {
    name: task.name,
    created_at: task.created_at,
    due_on: task.due_on,
    status: task.status
  })
}

  deleteTask(task: ITask) {
    return this.delet(`http://localhost:8000/api/tasks/${task.id}/`, {});
  }

  createTask(id:number, name: any, created_at: any, due_on: any, status: any): Promise<ITask>{
   return this.post(`http://localhost:8000/api/task_list/${id}/task/`, {
     name: name,
     created_at: created_at,
     due_on: due_on,
     status: status,
     task_list: id
   });
 }

 createTask2(task_list:ITaskList, name: any, created_at: any, due_on: any, status: any): Promise<ITask>{
  return this.post(`http://localhost:8000/api/task_list/${task_list.id}/task/`, {
    name: name,
    created_at: created_at,
    due_on: due_on,
    status: status
  })
}
 auth(login:any,password:any):Promise<IAuthResponse>{
   return this.post(`http://localhost:8000/api/login/`, {
     username: login,
     password: password
   });
 }
 logout():Promise <any>{
   return this.post(`http://localhost:8000/api/logout/`, {
   });
 }
}
