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
peers="ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,39429a15338825ea4fa6b310a7b12505e45b95d0@213.133.100.172:26858,91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,19bfc967641d29299d22a2510db8022b8f986db9@5.181.190.138:26656,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,815e9378b05a40e4a774223b55f5c6b8457a1c79@31.220.79.166:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.12.196:26656,d68d0ce3a3959f09ea935cffbf1cd282dcfec401@27.72.126.82:26656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,253dd70d480909a343d7d8b157e1b194711c6a1e@167.235.85.60:56656,24971494b3a2045d26b111c85e1ea6baf15fece3@89.169.46.109:26656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,239a619834bc135fdc845611fc77737b726e26cc@65.109.65.163:20156,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,38a626dfc05c0d9756098349ce8ccd532496d6a2@65.108.206.118:61456,0da5e83ef55df6f1c6f8c15c69bdd42ee43fd253@144.76.99.100:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
