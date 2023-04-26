# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.9.8 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: lava-testnet.grpc.kjnodes.com:44090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:44656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:44659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (30)
```bash
peers="370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,1829486da26d7b88fb2a921798bb70f9218fc052@14.191.217.125:26656,3456c9ba0df46cbb526717d73fa51ff0ed9a53a1@95.216.14.58:60756,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,2c419186cd96b59fe8b3307c54c27d6805414aba@65.108.8.28:60756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,c0efea9152aed75fcf3022b8af45243818c59d6a@49.12.13.104:26656,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,5b337f7ba27e2fdd27918be18af93f8728034267@65.108.41.168:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,0d08a1b452e6d7ccdfbc9b54658b5f9ed24eff7b@135.181.138.160:29956,f0758765ef0350d5cbbdeebf0b8e84f76e21c46d@54.221.204.97:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,4ad3f3731073a016fa0c99118b2a5a2d313928f5@207.180.233.148:26656,c32d101819cedf78ea986e6d832e2306fb6d0649@185.248.24.224:16656,525696e557db51c4d5f5bca1d7152753c7426c2e@34.192.150.110:26656,230648adf4aa55029c72ec5d7bc1be59529acf34@37.120.171.159:26656,37692dcf03498b5f42217c14a40ceb4f771b5bd1@154.53.39.185:26656,9ff4aa1369a5759a05e0f8a40ebec5dae57735e9@135.181.161.235:26656,3d05c96b70553fa5feb5d088fb4c0e2f01b3ec4e@136.243.147.235:38656,697750a8171090e8547c1749ff05c88c080f6350@131.153.158.137:26656,9cad8c3a210ddd4cf6111ef0e03e7155570f27c3@155.133.27.248:26656,e48b71ec95d9638a90477288219805d3b0bab758@80.90.86.119:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
