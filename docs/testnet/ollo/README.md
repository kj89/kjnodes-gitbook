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

**live-peers** (24)
```bash
peers="dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,f09d8e2ada2d1d66a9cc8213a1d8ca7c6e5a29a6@65.108.79.57:54656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,742d7dccc98ccc2b30abb6ea172fc2175782db50@148.251.91.185:26656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,60a8fdd419c20f509cf590a10978827bcf1cf25c@161.97.99.251:11656,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,032845b1a798108bfc1fd91ebe5bdbbccd4a34d8@135.181.221.186:32656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,799dff05af5d30477f44c816753ff89104b2b8b5@116.202.227.117:32656,e709b708ea24ed8fefb5c82cc460bb485b403960@83.8.202.197:28656,b5f55cfc7b4d19f2dd3cdc71795f5a81e2c67f96@38.242.232.72:26656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,80c6ccc9523bd59a0420e76e8355f46fb61bf74f@65.109.93.58:33656,e8bdc07477c4a49acf1a4c91e3dc34fe2372169e@161.97.153.160:26656,cba0eacc21eaddadc8903d503b1db12dd002fd0f@65.108.226.183:18156,e2d59891f1aed38fe8884c63e0bb00f8ddc41b6f@5.78.46.66:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:18156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
