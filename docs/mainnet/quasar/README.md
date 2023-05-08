# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: quasar-1 | **Latest Version Tag**: v0.1.0 | **Wasm**: ON

[Website](https://www.quasar.fi) | [Discord](https://discord.gg/quasarfi) | [Twitter](https://twitter.com/QuasarFi)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/quasar](https://explorer.kjnodes.com/quasar)

## Public endpoints

* api: [https://quasar.api.kjnodes.com](https://quasar.api.kjnodes.com)
* rpc: [https://quasar.rpc.kjnodes.com](https://quasar.rpc.kjnodes.com)
* grpc: quasar.grpc.kjnodes.com:14890

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quasar.rpc.kjnodes.com:14856
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quasar.rpc.kjnodes.com:14859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quasar/addrbook.json > $HOME/.quasarnode/config/addrbook.json
```

**live-peers** (11)
```bash
peers="89757803f40da51678451735445ad40d5b15e059@169.155.169.149:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.169.84:26656,771659b9205187f9094f894c65d29effa79fdd2c@18.156.191.84:26656,a40e1d5f63fad9e14edb9c95458b27f3c1de858c@116.203.236.246:26618,8688b59432d98b6ded8bed01c3c29d4892ae6e4f@38.146.3.149:18256,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.170.222:26656,367d65ece0aafd9b46e15b9dd58fe319d7d29550@143.198.172.109:26656,97e4468ac589eac505a800411c635b14511a61bb@134.65.195.240:26656,8f74699ec25e0ab5a60911e21135a9a330da8399@50.18.180.161:26656,5a111b281852be31838ecf1202e59981e618355e@89.116.31.95:18256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:14856"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
