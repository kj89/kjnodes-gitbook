# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)




## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: [https://andromeda-testnet.grpc.kjnodes.com](https://andromeda-testnet.grpc.kjnodes.com)

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
peers="99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,38a546d75ae84bb002990ce2eb35c04d7d284809@159.223.69.214:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656,9d058b4c4eb63122dfab2278d8be1bf6bf07f9ef@65.109.86.236:26656,50ce639d8889108b488f0aa802468bc13d4873a4@75.119.159.195:26656,7fd9a427a03f0e8632d2ff4b6fe32e99e3151f04@23.88.71.247:31656,1c101b595362f6a5856ef34f43545cf95eb34912@65.109.26.21:15656,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,f3d598517ea86c08236b53882338b0b5e1d0f0e8@213.239.207.175:42656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,0fd8550e58b1e450b40032e17ca6d685f7be1c53@217.160.201.92:26656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,bb81a52f86a5332e447373796f8a0b99f195816d@5.78.67.243:26656,1c9d70cda1b46e8a33a39783e9af0ad8b5d876ac@65.109.85.225:3340,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
