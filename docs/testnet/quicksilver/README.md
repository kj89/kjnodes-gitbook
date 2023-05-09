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
peers="a637b94cb989909cc182623748ef179b0659f148@65.109.23.114:11156,0ccfc2136005f448c11dd515e22aac3e25f4b6dd@31.220.84.183:36656,7781c28c240e85474425040f744b501d99120d1d@195.201.108.152:11656,25410bff2fb7312d24c11b1e990507e5e3aa40b7@135.125.5.31:48656,ee6bae1a6d4a1e07f1e4bc7963cabedc6b73426e@94.130.137.119:26656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,858ba6bc33a6d13fdd9ddad344d788dcf91cf565@142.132.151.99:15651,5844010472bac487748336616d450bc9f0cbc57c@65.108.72.175:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
