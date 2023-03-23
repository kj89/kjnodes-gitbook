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
peers="67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,47655c33bdecae7f449301197d8b951a97e1b680@89.58.59.75:26656,036d17d15c4e36cee8d93f9fb1a5ad5cb956631f@213.136.76.191:26656,125b0e30f00df3ff2ee7b29b7992ed888998ad31@65.109.28.177:47656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,742d7dccc98ccc2b30abb6ea172fc2175782db50@148.251.91.185:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@188.165.221.155:30595,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,4b73754c2c10d523ffd43ca95d9cb6e0ad8204a4@5.189.148.147:26656,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,80c6ccc9523bd59a0420e76e8355f46fb61bf74f@65.109.93.58:33656,a9123ae1e1b7f8438e7262efd50031aab600df41@154.12.225.160:32656,b1fe199b7ac2a7714c5d21524bb87810a2be94fb@135.181.178.53:32656,93085f2731cabd480d9b61397d3e1cf84f5a023b@168.119.124.130:32656,b5f55cfc7b4d19f2dd3cdc71795f5a81e2c67f96@38.242.232.72:26656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
