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
* grpc: quicksilver-testnet.grpc.kjnodes.com:11190

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver-testnet.rpc.kjnodes.com:11156
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="d4d83e209a2b096859821228ea17475f9a487a48@23.88.0.170:15651,13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,25410bff2fb7312d24c11b1e990507e5e3aa40b7@135.125.5.31:48656,a637b94cb989909cc182623748ef179b0659f148@65.109.23.114:11156,74abcb5243d4ffc43de6ad1a288d8e50adcd467e@65.109.80.176:20656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,7781c28c240e85474425040f744b501d99120d1d@195.201.108.152:11656,0ccfc2136005f448c11dd515e22aac3e25f4b6dd@31.220.84.183:36656,796e72ffc343c187cd5e8397c0c09c0671d228e0@185.16.39.51:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
