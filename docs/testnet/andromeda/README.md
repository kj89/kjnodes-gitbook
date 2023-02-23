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

**live-peers** (9)
```bash
peers="3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,ef6ec2cf74e157e3c6056c0469f3ede08b418ec7@144.76.164.139:15656,50b339cce229121d5f4c710e4db01eafb17f95d6@161.97.175.56:36656,bcef415d908dfc5c7caff3325eefd51a730695b4@65.21.92.46:30656,a9d237b5070c7790a57318aa2bbe9b4f4f04cce2@194.163.175.163:30656,c043b90a737b92b26b39c52c502d7468dc6b1481@46.0.203.78:22258,95e8225c5b8a21c1fecd411f37c75f5515de1891@185.197.251.203:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
