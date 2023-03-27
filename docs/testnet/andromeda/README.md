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

**live-peers** (19)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,360ab15495b087bc27d134418dcd9191dec07c12@46.175.148.142:26656,8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,cc1c2cd585792d81a041e9098e36814dc8d1e6ae@213.239.207.165:28756,e95899eb682e517d74449dd575073daf1a3266d5@135.181.208.169:27656,ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,1c9d70cda1b46e8a33a39783e9af0ad8b5d876ac@65.109.85.225:3340,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,bcef415d908dfc5c7caff3325eefd51a730695b4@65.21.92.46:30656,df7cf95427701d6d00797042fb8548a7f8eeeb6e@172.104.159.69:55716,7fd9a427a03f0e8632d2ff4b6fe32e99e3151f04@23.88.71.247:31656,d30a56dd61de5b3e8d36bf40cb0a15add3915c91@195.3.223.33:37656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,3322611985d1c6df9fa8da141887eeb0c473ae41@95.217.164.130:26656,b594f01b5b49a11b6d2e97c3b6358dc1388a1039@65.108.108.52:26656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
