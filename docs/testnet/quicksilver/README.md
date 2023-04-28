# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-5 | **Latest Version Tag**: v1.4.0-rc10.2 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/quicksilver-testnet](https://explorer.kjnodes.com/quicksilver-testnet)

## Public endpoints

* api: [https://quicksilver-testnet.api.kjnodes.com](https://quicksilver-testnet.api.kjnodes.com)
* rpc: [https://quicksilver-testnet.rpc.kjnodes.com](https://quicksilver-testnet.rpc.kjnodes.com)
* grpc: quicksilver-testnet.grpc.kjnodes.com:11090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver-testnet.rpc.kjnodes.com:11656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (28)
```bash
peers="9a60250367f370dc7395c7a5b0d503cec544188f@65.108.230.113:20026,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,e25a748120c9608c1d2a70fafa75178d862b3463@178.18.254.211:10656,1c4274460224753e8080d0efd16c0ed88fe27fc0@51.195.145.103:26656,a637b94cb989909cc182623748ef179b0659f148@65.109.23.114:11156,0ccfc2136005f448c11dd515e22aac3e25f4b6dd@31.220.84.183:36656,0551eaa0db7097274410ee27a71672817e314b83@167.235.245.191:26656,f0621c59ca7cfba98015ae2a47886fc3d9c0020c@94.130.132.227:2060,a49d8d304e96350272dca24934b8295bc81d75d2@23.227.200.10:26656,42f87cb55d5fdd222da28023613c66857398c4b8@5.22.223.252:26656,a288baa951cbe92b253c01c3936d930af1d56424@5.161.142.236:26656,af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,d4d83e209a2b096859821228ea17475f9a487a48@23.88.0.170:15651,c9a74cdd754a8ccc9243ac2b245e4caaa78695aa@45.85.147.96:26656,03332cdbc3d354846a18992effbb8c20aa28f52a@65.21.133.125:28656,78d271e4b4692ff1ee8490f3825a541558b31870@65.21.95.46:28656,17d1c0845076139a81174b1837bff598fb255d31@46.4.121.72:11156,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,796e72ffc343c187cd5e8397c0c09c0671d228e0@185.16.39.51:26656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,025e1a9ba7e536e1db47569b55081f7adf6d2f9e@95.217.83.28:26636,97377c16946f8e1fa69e7c2c6b7feb32c2090f09@116.202.227.117:11656,2aed12a25bfa92e40ccb95c88692735a9488a17e@65.109.92.79:37656,78acdbabc08231765444b3143a222d433a5157e1@142.132.205.94:15651,25410bff2fb7312d24c11b1e990507e5e3aa40b7@135.125.5.31:48656,7781c28c240e85474425040f744b501d99120d1d@195.201.108.152:11656,ac6068dc650358a0c8f7b774630367ba2c70fa1f@93.190.141.68:21026,d0d0903d8c2f514c92284341d48aa422d4e37740@78.47.198.121:21026"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
