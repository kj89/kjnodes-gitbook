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

**live-peers** (9)
```bash
peers="0ccfc2136005f448c11dd515e22aac3e25f4b6dd@31.220.84.183:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11156,e25a748120c9608c1d2a70fafa75178d862b3463@178.18.254.211:10656,13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,7781c28c240e85474425040f744b501d99120d1d@195.201.108.152:11656,5844010472bac487748336616d450bc9f0cbc57c@65.108.72.175:29656,d4d83e209a2b096859821228ea17475f9a487a48@23.88.0.170:15651,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,03332cdbc3d354846a18992effbb8c20aa28f52a@65.21.133.125:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
