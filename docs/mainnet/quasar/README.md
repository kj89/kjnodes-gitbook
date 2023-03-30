# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" width="150" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: quasar-1 | **Latest Version Tag**: v0.1.0 | **Wasm**: ON

[Website](https://www.quasar.fi) | [Discord](https://discord.gg/quasarfi) | [Twitter](https://twitter.com/QuasarFi)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/quasar](https://explorer.kjnodes.com/quasar)

## Public endpoints

* api: [https://quasar.api.kjnodes.com](https://quasar.api.kjnodes.com)
* rpc: [https://quasar.rpc.kjnodes.com](https://quasar.rpc.kjnodes.com)
* grpc: quasar.grpc.kjnodes.com:48090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quasar.rpc.kjnodes.com:48656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quasar.rpc.kjnodes.com:48659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quasar/addrbook.json > $HOME/.quasarnode/config/addrbook.json
```

**live-peers** (20)
```bash
peers="a40e1d5f63fad9e14edb9c95458b27f3c1de858c@116.203.236.246:26618,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:48656,d11f867df7e498de0835e2d1b5bc34334c7337d1@65.109.31.114:2490,89757803f40da51678451735445ad40d5b15e059@169.155.169.149:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@134.65.192.124:26656,619fc43aceebc5a9f70c6ea95ad2a94319294a54@141.95.103.138:26656,b5d43d295863db6675d07877878b2d7b47cb2ae5@157.90.36.48:26966,5a111b281852be31838ecf1202e59981e618355e@89.116.31.95:18256,d7ea38275af96271fd66194dad3951ef38b8ba7c@193.70.33.64:18256,e62ce06e60a986ed04d2e080876a41e3b57a5304@93.190.141.218:26656,240c09f5d91d2c252cf29faa1a88aebd563d2561@57.128.144.247:26656,58a4943a150cc77ab77ded222c44b23548ee702a@146.59.81.23:26667,66e0a7d2c2fc75a91627085d0ac5681a35dfd408@37.252.184.234:26656,4399187c748f91d86932d3e530cd16c22c5f616a@199.231.163.42:26656,83f4a463b8130b9ccf3bc96f80ac213a9a856dfc@34.27.99.121:26656,88cc4d314c9804a9478e900b6f18a83ea58a98c6@57.128.20.163:18256,8688b59432d98b6ded8bed01c3c29d4892ae6e4f@38.146.3.149:18256,2b01cb4d5c2108b20788aad68e11149899f170f4@99.80.59.242:26656,471518432477e31ea348af246c0b54095d41352c@134.65.195.144:26656,6cceba286b498d4a1931f85e35ea0fa433373057@169.155.170.222:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
