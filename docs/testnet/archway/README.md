# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/archway.png" alt=""><figcaption></figcaption></figure>

Archway is an incentivized smart contract chain for Cosmos  ecosystem which gives developers a simple way to build  scalable cross-chain dapps. The developers automatically  receive rewards for their contributions to the network.

**Chain ID**: constantine-2 | **Latest Version Tag**: v0.4.0 | **Wasm**: ON

[Website](https://archway.io) | [Discord](https://discord.gg/archwayhq) | [Twitter](https://twitter.com/archwayhq)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/archway-testnet](https://explorer.kjnodes.com/archway-testnet)

## Public endpoints

* api: [https://archway-testnet.api.kjnodes.com](https://archway-testnet.api.kjnodes.com)
* rpc: [https://archway-testnet.rpc.kjnodes.com](https://archway-testnet.rpc.kjnodes.com)
* grpc: archway-testnet.grpc.kjnodes.com:15690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@archway-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@archway-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/archway-testnet/addrbook.json > $HOME/.archway/config/addrbook.json
```

**live-peers** (10)
```bash
peers="da7d8ff27d6aa891f54f0a6647dc0bd5ae1e7b49@116.203.35.46:46656,ed7125298aa07ab9741dfe228dce937c3e53f396@185.52.52.26:26656,e40e240706e5c551de40fefab1ad9fbf4a4bec23@141.94.73.39:42656,8df8a64ecf0aaba1e1faee06d005aa912d578549@65.109.89.5:41656,c8171d5b90ea72992408f8cfcd3893256d22aabc@65.109.94.221:40656,1413664d3cfa37c2d661f740b2b47105433f3872@65.21.139.155:34656,a05590886e3d3b0baa7a605ef2ee00db689308b8@35.238.216.151:26656,85c669e01f5fca4d1ef7636a9526296a0083bb1d@15.235.193.57:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,a77c935197691d0d526fcb65a08df364a96bea9b@142.132.134.112:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.archway/config/config.toml
```
