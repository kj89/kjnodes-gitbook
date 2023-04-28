# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/juno.png" alt=""><figcaption></figcaption></figure>

Juno is a global, open source, permission-less  network for decentralized interoperable applications.

**Chain ID**: juno-1 | **Latest Version Tag**: v14.0.0 | **Wasm**: ON

[Website](https://www.junonetwork.io) | [Discord](https://discord.gg/qJxgUSGHbb) | [Twitter](https://twitter.com/JunoNetwork)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/juno](https://explorer.kjnodes.com/juno)

## Public endpoints

* api: [https://juno.api.kjnodes.com](https://juno.api.kjnodes.com)
* rpc: [https://juno.rpc.kjnodes.com](https://juno.rpc.kjnodes.com)
* grpc: juno.grpc.kjnodes.com:57090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@juno.rpc.kjnodes.com:57656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@juno.rpc.kjnodes.com:57659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/juno/addrbook.json > $HOME/.juno/config/addrbook.json
```

**live-peers** (13)
```bash
peers="6b55539058ec85bcc38abb53604e0fa679336261@65.108.64.107:26656,e78c04f8d58e990c8748c4cf0dae85c6a077b690@65.21.227.95:2002,169022205f5811e2a0b31b6d3cf11e8a6dfb8242@116.202.192.156:26656,285b8d9cabcc9423b419c603c9d5e4cf216082e0@74.118.140.100:26656,5292be1e0829141ce28e01de3234a2060d592802@198.244.176.186:36656,6ee6fc1625a854214a01b48b959a48493097f437@94.130.68.212:26686,34aaa6b0eac3cb0b6f8d0ecb1795d7b50239b6bf@65.108.121.251:26656,069e299debe27f6d693e7a0703232067d63da683@51.81.107.95:10556,ccd92f5a25ca3f6ac6b0daa81f7d213a4767abb9@65.108.77.220:2000,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:57656,a6955453548eb1bcaf1edaabc171b6c3bef2ff37@95.216.4.104:6006,60493cb0f123f7717bfcb4432539a0a37a02df97@65.108.64.5:26656,8f3cbef6dc58d31bb70655d3d3c40d66d4744033@137.184.32.93:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.juno/config/config.toml
```
