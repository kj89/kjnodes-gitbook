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
peers="f277d5a80e789ce69bb3318dfd5efea45986c073@176.9.22.117:31656,55b3cf307182091e60b774712733231a8cc7f448@89.163.132.156:31656,0c6758a3f4554bbc67da73993bbb697764c5c534@38.242.142.227:26656,620478e35ba6740f0afb2a0dd6ca9b34765bc60e@65.109.30.12:60856,1dae68f061204fe2c10e9476239c0333258889e7@65.109.31.114:2460,d92268c246e02a54103f7098b901b876c88f006e@5.161.130.108:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,1380864bb38481fef4b2358026a5ed53fc027679@95.214.52.206:26656,2c0379f78b655e8a386cb477e3cf3cae700c4a7f@213.239.207.175:34656,ce6686036f6554deb0490103dcc201172e7c3f2f@81.0.220.131:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
