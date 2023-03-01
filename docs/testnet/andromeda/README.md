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

**live-peers** (10)
```bash
peers="aeccd559d0d6f8dfb4efcf311fbad3e80ae0e87f@217.160.26.225:26656,4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,00cedd85b1f6a2c859a8c6116b9578e1cc2623c6@51.222.44.116:30656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,c66e5cc02d87731faf781463466bf39723d4558b@68.183.181.120:26656,bb81a52f86a5332e447373796f8a0b99f195816d@5.78.67.243:26656,bcff023220351ee4c00b4c6c6f5118c0bca941fb@194.163.162.87:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
