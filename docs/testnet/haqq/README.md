# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.0 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)


## Public endpoints

* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:35656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (30)
```
peers="de231cd155362b2687dca190a744bf839ce4ce63@23.88.112.123:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,9af0d63f02475fc5c4cf60723070ea735895b626@185.119.59.223:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,125063c422e09faf45b849dd73dea61f624db891@65.109.53.60:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@34.90.129.213:26656,26f20a2f80a4738a30a9634947a3aae67da31be3@65.108.254.227:26656,e528bdb078e26ef6c10b0b8b571c5140f41e4fee@146.190.115.53:35656,d648d598c34e0e58ec759aa399fe4534021e8401@109.205.180.81:26656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@34.91.81.33:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,306ce653d6f0c77936b681d4ee8bbf66a4b8bb75@88.208.57.200:60956,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,c2e099196ba2dcebed50c66393a79bc13b43b698@78.29.44.119:26656,7094f2c1ee04801b76159bd614eb5947ffc8c5d9@109.71.177.3:35656,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,e576d332451c7c3c0c5c753b1bbd4e670b1ecfc7@5.161.97.83:26656,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,62d44513c7fd5aafa65773e5c015ca032f8eea4a@213.239.213.179:26656,99a8389c84625503c2b8d734dfd78035d28e4f15@65.109.30.117:26656,aed7038b96314fcb741168869c66029e6c6a58ef@34.90.39.222:26656,fed6ab9973f224f3b2334fd48fa835512d6311da@185.244.183.200:26656,ea0193fe956e6db31609202457600e901b29a7c0@146.190.51.155:35656,9e901f9b0f75d674e1df52b7474b3dd15ddaeb05@146.190.51.164:35656,b72f2156db8c87e679dc853730746ff40038120c@213.239.215.77:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
