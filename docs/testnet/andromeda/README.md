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
peers="8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,9d443f465ad66671d109142715e62ef8039cf0f8@161.97.85.248:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,debdccc98a2f6ed72561d7866381003903197935@144.126.142.78:29656,a4d291d17d8e74979e7db5a1e936269835e802af@194.165.59.78:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.12.196:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,b72a182c0c50e3425dc17fb7cc7f9215ae096461@46.149.79.196:26656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,27e4aeaf8ef79a25904cd1042cf25ac6a1a0e7e5@103.180.28.220:26656,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,7c9e768cdaa68d5c27b49797284acbd9d0dd9716@79.137.248.65:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,38a626dfc05c0d9756098349ce8ccd532496d6a2@65.108.206.118:61456,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27126,ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,24971494b3a2045d26b111c85e1ea6baf15fece3@89.169.46.109:26656,00c49b6c8f0613bda77f27bf5072e4a000ace2b7@89.252.21.37:60556,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,f66bcec970aaaaa9ae33182802ac4bf87b3b20cd@84.46.254.82:26656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,1becb7d86cfeddfc255c54243023fa4cdda0c3ee@31.222.238.170:26656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,c6c7256d80a5428aa1ab49a0417f9eb8422e8468@77.232.40.31:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
