# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (29)
```bash
peers="af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,25410bff2fb7312d24c11b1e990507e5e3aa40b7@135.125.5.31:48656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:27026,bdb93c655989b2c1882339fabb013317066dda56@95.214.52.138:26676,e25a748120c9608c1d2a70fafa75178d862b3463@178.18.254.211:10656,1c4274460224753e8080d0efd16c0ed88fe27fc0@51.195.145.103:26656,42f87cb55d5fdd222da28023613c66857398c4b8@5.22.223.252:26656,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,a49d8d304e96350272dca24934b8295bc81d75d2@23.227.200.10:26656,f0621c59ca7cfba98015ae2a47886fc3d9c0020c@94.130.132.227:2060,a637b94cb989909cc182623748ef179b0659f148@65.109.23.114:11156,13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,9a60250367f370dc7395c7a5b0d503cec544188f@65.108.230.113:20026,78d271e4b4692ff1ee8490f3825a541558b31870@65.21.95.46:28656,d4d83e209a2b096859821228ea17475f9a487a48@23.88.0.170:15651,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,97377c16946f8e1fa69e7c2c6b7feb32c2090f09@116.202.227.117:11656,0ccfc2136005f448c11dd515e22aac3e25f4b6dd@31.220.84.183:36656,a288baa951cbe92b253c01c3936d930af1d56424@5.161.142.236:26656,03332cdbc3d354846a18992effbb8c20aa28f52a@65.21.133.125:28656,025e1a9ba7e536e1db47569b55081f7adf6d2f9e@95.217.83.28:26636,796e72ffc343c187cd5e8397c0c09c0671d228e0@185.16.39.51:26656,1452d484454c0f93ddf3cbf987ce1b9cadd8f23f@65.21.95.180:37656,17d1c0845076139a81174b1837bff598fb255d31@46.4.121.72:11156,392a7ec2683e288866c353b7a8ac9ecc4e7b4bfc@142.165.207.19:16656,66f9d8f52a4637dc9215cdaa8dc2977633e52bbf@157.90.176.184:16656,74abcb5243d4ffc43de6ad1a288d8e50adcd467e@65.109.80.176:20656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
