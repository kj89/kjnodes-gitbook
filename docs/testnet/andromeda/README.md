# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (13)
```bash
peers="f1bca379ca2f358ddb39a69fdb0c9755903aeba8@80.76.43.138:26656,4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,7ff2aaa5c49a0907e52689cc90fa416ec70e06a4@185.245.182.152:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,bb81a52f86a5332e447373796f8a0b99f195816d@5.78.67.243:26656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,0cc98f28ed826b3b43d2c88deb214ff01b36f6ce@159.69.126.18:15656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
