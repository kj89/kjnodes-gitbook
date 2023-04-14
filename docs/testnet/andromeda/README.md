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

**live-peers** (29)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656,a5f70c6cbcf4dd17f68237d2b1fe3e34564cb1dd@80.76.43.138:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,fd48e41b990c9ba2cdd3e2f5adf20b8ab237b328@1.15.110.177:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.20.220:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,85e8cba341f2749d77d134464b44214a44ff327b@14.191.94.77:26656,8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,93e418796bf3b5d8cd319983269c99db83cb2ba6@5.161.78.48:16656,505b62b16c6e11f6cced2f3f8283d08862bdc822@164.90.208.147:26656,f51b215535e43428b7122c3d3ebbb4ab20c1b808@185.9.144.138:26656,20373ec71cffdb678099ca411fb862537f264791@178.172.212.135:26656,ce3a765f7075f3f5aee80bca0c76ca7dbe235731@167.235.198.193:36656,7469fd307adba5d8e782908ee01f080f3e554c48@185.154.13.19:26656,52ebde00c016f5f139e57eeca41b1f681647d23f@109.123.242.208:26656,139e89b8868aed5c5922a563ecd5002959af04ff@65.108.111.236:55716,086dd26d09ee6ff66307555cb9a25e0df76f377f@65.108.199.206:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
