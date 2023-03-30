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

**live-peers** (31)
```bash
peers="036d17d15c4e36cee8d93f9fb1a5ad5cb956631f@213.136.76.191:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,47655c33bdecae7f449301197d8b951a97e1b680@89.58.59.75:26656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,bc73e1f3bde267171309e723416690c9c7404881@142.132.199.236:27656,f09d8e2ada2d1d66a9cc8213a1d8ca7c6e5a29a6@65.108.79.57:54656,70ba32724461c7ed4ec8d6ddc8b5e0b1cfb9e237@54.219.57.63:26656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,0bee9e500e51465917506b47691a8fb032100da9@94.130.200.168:32656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,742d7dccc98ccc2b30abb6ea172fc2175782db50@148.251.91.185:26656,ab89596768849d679ed11a9e1848224760a278cc@83.171.248.175:32656,6fb1ca4b01926c43fb28f5eadc4710d0e7df8624@176.126.87.165:26656,29b78da822388df177f4111e6589958d9f796f06@65.109.122.105:60856,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,0f99f7481a1b49701866ddbdfe71dc3b2fd792d8@109.123.244.56:26626,799dff05af5d30477f44c816753ff89104b2b8b5@116.202.227.117:32656,76035e4e4afa5d7e560c57f27bb147504cf33dac@136.243.136.241:11656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,95ca646da3736cef5d6c6704f736bc49ff87ef6c@109.123.249.213:26656,60a8fdd419c20f509cf590a10978827bcf1cf25c@161.97.99.251:11656,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
