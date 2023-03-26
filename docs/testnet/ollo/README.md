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
peers="7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,742d7dccc98ccc2b30abb6ea172fc2175782db50@148.251.91.185:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,0f99f7481a1b49701866ddbdfe71dc3b2fd792d8@109.123.244.56:26626,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,70ba32724461c7ed4ec8d6ddc8b5e0b1cfb9e237@54.219.57.63:26656,b1fe199b7ac2a7714c5d21524bb87810a2be94fb@135.181.178.53:32656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@188.165.221.155:30595,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,4b73754c2c10d523ffd43ca95d9cb6e0ad8204a4@5.189.148.147:26656,771cfca799033e327511b25ae77784e02818d77f@65.108.101.4:23486,e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,c2bc7720a610d753b037d89e6c3f58f7c718e24f@116.202.117.229:32656,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,799dff05af5d30477f44c816753ff89104b2b8b5@116.202.227.117:32656,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,e2d59891f1aed38fe8884c63e0bb00f8ddc41b6f@5.78.46.66:26656,595a8418f3f68a499a873148ec19a95b0f34390c@65.109.82.106:32656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
