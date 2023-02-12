# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)




## Chain explorer
[https://explorer.kjnodes.com/ollo-testnet](https://explorer.kjnodes.com/ollo-testnet)

## Public endpoints

* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)
* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* grpc: [https://ollo-testnet.grpc.kjnodes.com](https://ollo-testnet.grpc.kjnodes.com)

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

**live-peers** (25)
```bash
peers="60a8fdd419c20f509cf590a10978827bcf1cf25c@161.97.99.251:11656,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,0f99f7481a1b49701866ddbdfe71dc3b2fd792d8@109.123.244.56:26626,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,084a8a6866edb7ed571e5b5f023be580e5673fee@95.165.89.222:24646,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,799dff05af5d30477f44c816753ff89104b2b8b5@116.202.227.117:32656,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,0d642afa8df369a5021609c43bb7765a332a615f@65.109.106.91:17656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,c0b03cf21640b12d78f6b4b50d7505d05d37f055@95.217.230.54:26656,ab89596768849d679ed11a9e1848224760a278cc@83.171.248.175:32656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
