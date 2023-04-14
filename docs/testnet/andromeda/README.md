# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:47090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (30)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656,13eff3f60e60546435a9f79e241372b299f559a1@5.161.80.223:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.20.220:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,7469fd307adba5d8e782908ee01f080f3e554c48@185.154.13.19:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,fd48e41b990c9ba2cdd3e2f5adf20b8ab237b328@1.15.110.177:26656,cc1c2cd585792d81a041e9098e36814dc8d1e6ae@213.239.207.165:28756,fc86695b94a32014df458ba0acf37a5954ef6575@82.146.57.121:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,5e5186020063f7f8a3f3c6c23feca32830a18f33@65.109.174.30:56656,3c5024a2213f8bae01e85f450e3d5eb11cf28768@95.217.188.65:26656,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,41681200a0e60e9477181db813e1894684020378@194.233.92.77:26656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,5cfce64114f98e29878567bdd1adbebe18670fc6@65.108.231.124:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
