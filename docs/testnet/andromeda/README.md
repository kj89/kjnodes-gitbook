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
* grpc: andromeda-testnet.grpc.kjnodes.com:14790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:14756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:14759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="04f999a256386af81147442b05ffd4022313de2c@146.190.116.68:20156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,57accd1be23702a5b374f84e990d85e4ddac47c8@142.132.237.91:20156,94fdba93b79d27701896d65d8e60155e06326532@65.109.63.110:15656,1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,8eaf3fcfe6c081465d4b3a3530cd53d3d8a4a760@62.171.128.14:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,debdccc98a2f6ed72561d7866381003903197935@144.126.142.78:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
