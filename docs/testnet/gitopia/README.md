# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

Website: [https://gitopia.com/](https://gitopia.com/)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (24)
```
peers="3e5ba61e8481c6c71d3f2cc022dd6671ed7cacf8@65.21.170.3:41656,a6459b8c3e221e9e0ffd30d8cc883bb2d2d5859f@95.217.16.89:41656,34f5ee00693e05cff3f4fb5d1ca02cf4f254b05c@65.109.84.254:60956,d9d59b442e46f142394fcdf2f246ca8c7b2b7ce9@149.102.146.36:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,4570f274ac45e9ab114d5a467e18fa29a305b25f@135.181.1.109:41656,c83b73dea4060655443a7bacf3d456608f0d8535@65.109.30.12:36656,f3dd86f60c19da51e88a9378d3ae8c2892c456ad@150.230.102.178:2536,a47375da7f790427c69103d363e4f8de4a6acfac@5.199.143.159:36656,212f50ece90eb53b95b0115600bea233e0c5bec1@65.108.124.54:34656,ed9e3ea0d633fa27690f5d4db039403bbb1aeba8@165.22.214.209:26656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,fccf79904b3c03488955d580509d0cc65bb3bb56@65.21.104.192:26656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,37677351ed74a5ced46a99217d19e30d5bcacc1d@5.75.147.138:26656,3e10c9f1ae075b7e8051a49927667b7b21186a66@80.241.220.28:46656,f6eeb6fa84ec13380f420af84fc293d00ad614ad@185.202.223.189:41656,cf31f6db36843f04675d694e6d79874d6acc3331@38.242.208.177:26656,8a20f16d02806ba11bf9fab1fca91830578faa9e@161.97.151.46:46656,4977214dacb3713797653c1bc07b5982bcc91649@142.132.253.112:51656,a536f71fcc2497cc7f8ef2b74b43368eaf3bf1b8@65.109.51.41:60956,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,5171aad5f862d474b36fc8049be3339068c96cc9@165.232.151.144:26656,51c3b05112f73a6e60e8b2e96d5528a39a3f4e5e@38.242.246.96:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
