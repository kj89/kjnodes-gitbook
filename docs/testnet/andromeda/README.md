# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" alt=""><figcaption></figcaption></figure>

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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,c89e274523cec4a7445afaff1ab35029b090ff5b@65.109.116.204:20156,385bda41dc8ce86d0dd4c99d3cf371ca8fccfeb6@135.125.189.131:20095,ef8045e2922cf856b73f5fa5efdb79f925204ccf@65.109.117.159:15656,9e14886f7a34c73e65eafb209a9215e2848e9e76@65.108.41.172:29456,05d3613dfb738ff22d0ea974bd0d1353ecdc6231@65.108.101.124:26656,9230896c5f22a363eed1c3bd3ed8068134b1dedd@124.120.21.244:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,00171178f5d8b22d1a3396d9388adbb8ec1c0541@38.242.208.162:36656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,fb7db0edee4ee43c2c65a81fd33e201c758d93df@137.184.176.247:47656,7649ae1ea0dd5f640ac7dd7632a0866cf65e3aa4@31.220.90.78:26656,362ede6f335ed641e9eba0057bc1d98b391751dd@65.108.54.29:26656,54188a9dea5ded1d891aa6c3c0e2a403322b1707@178.54.78.180:16656,05b853c6022c51b2065665e66876e27aee9fed59@149.102.140.189:26656,1141119a7d248cc19b31b18d56162a365954deb9@45.132.106.149:26656,85953732c4eb5165724ac6db331240ff0815daf1@1.15.104.210:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656,e95899eb682e517d74449dd575073daf1a3266d5@135.181.208.169:27656,bf7b1bc3316af03223eeabf8e9eef8ccaa5d48d4@65.108.149.12:26656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,d3ac63ff921486f8aef1eba7870cae1d14c38633@1.15.146.92:26656,6d59b44efa40c4a03a24bf598b6cd662e8003655@135.181.96.66:26656,67794c8e6111f4356fdd7f7544e32e32a06b84de@194.146.13.180:26646,e063bf68a71f0f66a69772cfcfc29e3efc69c21a@95.216.185.202:26656,7002fb6369cd13f8aa1520fd7a81e67a9adf2636@185.119.196.39:26656,7ba9cadf6197c30fa808d9315333054ef953be9c@144.76.164.139:15656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,fd48e41b990c9ba2cdd3e2f5adf20b8ab237b328@1.15.110.177:26656,92f3e3d6652061c21b42985cab7aaec65ed1eb73@164.68.115.227:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
