# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.2.2 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nolus-testnet](https://explorer.kjnodes.com/nolus-testnet)

## Public endpoints

* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)
* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* grpc: nolus-testnet.grpc.kjnodes.com:43090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (27)
```bash
peers="b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,78988c94a1a8f37b8995c7794d103e2979cefd2e@5.75.231.119:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,646d17dc6126bfe79eaeb2b95964323f198c9d3c@65.109.53.60:28656,fac035258738be9be98957d5d012d24841d2e5eb@85.10.197.4:16656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,73176af073e4f89609db7aa4ec3561ce1b98d308@85.10.193.246:32656,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,73e55e512de96e81fa025463f1581daf64172f76@65.108.13.154:31656,2fc6d24d1d77c34427ce7cbb24de5ee4d4debe7c@161.97.108.208:26656,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,538e2a3d6e96cd7bc0635eaa3f8f3695f26503a7@65.108.104.167:21656,4cf9c28f20faac9baae74870cb52bae590dbd81e@65.108.228.96:26656,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,ca83b6457bfce88d892646b6afb51165ec3e94d4@135.181.183.93:22656,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
