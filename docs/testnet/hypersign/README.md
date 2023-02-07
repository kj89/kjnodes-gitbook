# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

Hypersign is a decentralized identity layer for the internet, giving  users control of their personal data and identity whilst digital  enabling trust for businesses.

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.5 | **Wasm**: OFF

[Website](https://hypersign.id) | [Discord](https://discord.gg/DmuUjMrHVw) | [Twitter](https://twitter.com/hypersignchain)




## Chain explorer
[https://explorer.kjnodes.com/hypersign-testnet](https://explorer.kjnodes.com/hypersign-testnet)

## Public endpoints

* api: [https://hypersign-testnet.api.kjnodes.com](https://hypersign-testnet.api.kjnodes.com)
* rpc: [https://hypersign-testnet.rpc.kjnodes.com](https://hypersign-testnet.rpc.kjnodes.com)
* grpc: [https://hypersign-testnet.grpc.kjnodes.com](https://hypersign-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@hypersign-testnet.rpc.kjnodes.com:31656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@hypersign-testnet.rpc.kjnodes.com:31659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/addrbook.json > $HOME/.hid-node/config/addrbook.json
```

**live-peers** (10)
```bash
peers="c20f2216b56cb24921b688a6cffc7fe09799a069@162.55.103.44:26656,0c6758a3f4554bbc67da73993bbb697764c5c534@38.242.142.227:26656,620478e35ba6740f0afb2a0dd6ca9b34765bc60e@65.109.30.12:60856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,ce6686036f6554deb0490103dcc201172e7c3f2f@81.0.220.131:26656,f277d5a80e789ce69bb3318dfd5efea45986c073@176.9.22.117:31656,9876d1b1e5b5968c1c729559325dd909f93c1d34@65.108.238.61:56656,d7c9b9a3c3a6c5f4ccdfb37a8358755b277271c1@3.110.226.164:26656,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,0188d0143ea4311923a809bb07ee9ebf13c0c63b@94.130.16.254:60656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
