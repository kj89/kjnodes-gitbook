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

**live-peers** (28)
```bash
peers="d8088d91bdbf2ccdf59f0b3ee1c1b07e8cb60798@195.201.237.185:11656,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,87e0efe332fdc4b0c2a76d18761a936509762067@212.41.9.98:36656,7042490bf1526d8c61c43ffe4d700388b73b905f@65.108.192.123:35656,8d59cbd6f8aa5c19613b1e64560f6024cde2ef81@202.61.251.135:26656,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,6c7df995fc208bf1e46b247eea141923868d9452@185.144.99.9:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,73e55e512de96e81fa025463f1581daf64172f76@65.108.13.154:31656,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,441ee01f2bb396bf4116f197e4d9eefbd88f5e10@65.109.122.105:60756,2c0ff6e5f30189559ad336a1eb17ae48fcacc8ee@95.216.14.58:61456,2fc6d24d1d77c34427ce7cbb24de5ee4d4debe7c@161.97.108.208:26656,60c57c5b7215c84260249768cf66ae550142af9f@141.98.169.25:26656,ca83b6457bfce88d892646b6afb51165ec3e94d4@135.181.183.93:22656,b4553ec94efe9cb11c684661042eedc2adf6ead3@23.88.74.54:42656,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,a95975f3a58e20ba1c518f3cbb1c23ef7569e4d4@14.241.82.87:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
