# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ollo-testnet](https://explorer.kjnodes.com/ollo-testnet)

## Public endpoints

* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)
* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* grpc: ollo-testnet.grpc.kjnodes.com:32090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:32656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:32659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (22)
```bash
peers="60a8fdd419c20f509cf590a10978827bcf1cf25c@161.97.99.251:11656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,47655c33bdecae7f449301197d8b951a97e1b680@89.58.59.75:26656,742d7dccc98ccc2b30abb6ea172fc2175782db50@148.251.91.185:26656,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,c2bc7720a610d753b037d89e6c3f58f7c718e24f@116.202.117.229:32656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,70ba32724461c7ed4ec8d6ddc8b5e0b1cfb9e237@54.219.57.63:26656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,ab89596768849d679ed11a9e1848224760a278cc@83.171.248.175:32656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,80c6ccc9523bd59a0420e76e8355f46fb61bf74f@65.109.93.58:33656,d94c9bf688c921319bf3747e41cc6bafd589ffde@65.21.134.243:26677,f09d8e2ada2d1d66a9cc8213a1d8ca7c6e5a29a6@65.108.79.57:54656,95ca646da3736cef5d6c6704f736bc49ff87ef6c@109.123.249.213:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
