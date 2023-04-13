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
peers="8a551bc0cc7ba190db9126c8fc95c8b643ae511c@195.201.174.109:56656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,a5f70c6cbcf4dd17f68237d2b1fe3e34564cb1dd@80.76.43.138:26656,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.20.220:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,cfab4a4226372d11bf95b4aa1b1ece4e610a2185@5.75.162.210:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,0da5e83ef55df6f1c6f8c15c69bdd42ee43fd253@144.76.99.100:30656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,93e418796bf3b5d8cd319983269c99db83cb2ba6@5.161.78.48:16656,505b62b16c6e11f6cced2f3f8283d08862bdc822@164.90.208.147:26656,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,5d076eccdbd1ae1835131be8e20b756e779c5bac@158.220.110.42:26656,ef30bb942109dbb6d1a13c3c32c46459689a6c15@162.55.245.219:19656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,855a1da5a4dc8381804b4a76158a69f41397447c@212.227.12.83:26656,41681200a0e60e9477181db813e1894684020378@194.233.92.77:26656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,6ef441d08cdb54b9f058884509ec65349976d73d@178.172.212.167:26656,d68d0ce3a3959f09ea935cffbf1cd282dcfec401@27.72.126.82:26656,5cfce64114f98e29878567bdd1adbebe18670fc6@65.108.231.124:30656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
