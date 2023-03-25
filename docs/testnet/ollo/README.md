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
peers="799dff05af5d30477f44c816753ff89104b2b8b5@116.202.227.117:32656,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,29b78da822388df177f4111e6589958d9f796f06@65.109.122.105:60856,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,742d7dccc98ccc2b30abb6ea172fc2175782db50@148.251.91.185:26656,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,ab89596768849d679ed11a9e1848224760a278cc@83.171.248.175:32656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,47655c33bdecae7f449301197d8b951a97e1b680@89.58.59.75:26656,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,2f5965450c9c831266959632fba2c1533b8f676d@38.242.248.2:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@188.165.221.155:30595,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,f2994f0ed16756151914ee95f041a7bff4f82b22@138.201.204.5:29656,a99fc4e81770ca32d574cac2e8680dccc9b55f74@18.144.61.148:26656,e709b708ea24ed8fefb5c82cc460bb485b403960@83.8.114.208:28656,80b1ad27820f58b49e7a5a68881f0248a6269e9b@65.108.132.239:15656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,e2d59891f1aed38fe8884c63e0bb00f8ddc41b6f@5.78.46.66:26656,e8bdc07477c4a49acf1a4c91e3dc34fe2372169e@161.97.153.160:26656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
