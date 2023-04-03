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

**live-peers** (21)
```bash
peers="3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,0bee9e500e51465917506b47691a8fb032100da9@94.130.200.168:32656,742d7dccc98ccc2b30abb6ea172fc2175782db50@148.251.91.185:26656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,60a8fdd419c20f509cf590a10978827bcf1cf25c@161.97.99.251:11656,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,a9123ae1e1b7f8438e7262efd50031aab600df41@154.12.225.160:32656,95ca646da3736cef5d6c6704f736bc49ff87ef6c@109.123.249.213:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,d94c9bf688c921319bf3747e41cc6bafd589ffde@65.21.134.243:26677,90ad9622ac54023fe4ee9824d77b5d3e3c25c245@162.55.234.70:54956,032845b1a798108bfc1fd91ebe5bdbbccd4a34d8@135.181.221.186:32656,cba0eacc21eaddadc8903d503b1db12dd002fd0f@65.108.226.183:18156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
