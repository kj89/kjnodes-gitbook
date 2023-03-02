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

**live-peers** (17)
```bash
peers="0fd8550e58b1e450b40032e17ca6d685f7be1c53@217.160.201.92:26656,50ce639d8889108b488f0aa802468bc13d4873a4@75.119.159.195:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,2e5ac443db5dc855bb33570ef58ce21cf130197f@82.208.21.15:36656,f3d598517ea86c08236b53882338b0b5e1d0f0e8@213.239.207.175:42656,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,1c9d70cda1b46e8a33a39783e9af0ad8b5d876ac@65.109.85.225:3340,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656,bb81a52f86a5332e447373796f8a0b99f195816d@5.78.67.243:26656,b9836aff6d8e79b9a04b4a2a80d6007bf33a526b@198.244.179.125:32069,334a842f175c2c24c6b11e8bce39c9d3443471ae@38.242.213.79:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
