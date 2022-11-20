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

**live-peers** (32)
```
peers="674a5a8d8f2a0815601bed562c46c060aa8ec075@65.109.70.4:60956,d2aa45ac84cf4136182f8012b974c3e1ba762eda@65.109.53.60:56656,76895e84873db23aa366296acc6900e1dd980f43@195.201.237.185:22656,75a9570b82474af11fc8c895f9da1ecb5da0c73f@95.216.143.237:19656,fccf79904b3c03488955d580509d0cc65bb3bb56@65.21.104.192:26656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,0d1a964bbe844ab45a0ec93ffed81945e588f6b9@5.161.86.214:26656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,669e77fe3452f7b25d9cb1e95696419f0d3481da@65.109.49.163:37656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,a6ef0e8544ee212cb6e571f8bc1562e7774bd2c5@88.198.34.226:11056,e8799d0034f6b99cc01916639dc424c7d2548784@185.169.252.60:36656,a47375da7f790427c69103d363e4f8de4a6acfac@5.199.143.159:36656,f584fdcb5a014e8b6b8e4a7cc9879dae35f14ff1@162.55.194.205:41656,2688adaacbf7ea5afb902f9fda9d10dfe9975a95@65.21.104.54:60956,527c0753c83a5a89f5b51f50151b51a0d8638f7e@113.30.189.23:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,fdeb051aae6f555150bb4cf685719879f21cd3e4@217.13.223.167:36656,56c544dc2cf49daddc5958976ba01b8719a06200@65.21.178.237:656,a536f71fcc2497cc7f8ef2b74b43368eaf3bf1b8@65.109.51.41:60956,cf31f6db36843f04675d694e6d79874d6acc3331@38.242.208.177:26656,05fa81c618612d6730cb8b54620954ce384899af@146.190.218.191:41656,3511b4bffe4d804065181625b32e2507934fdb05@82.208.20.137:26656,48691bfaddd58090c948e28d29156c2907b85ada@82.208.20.67:27656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,2853f7582257f0a19854072906e21eb694aa05b4@80.79.6.253:26656,72678266f62ab7f0e79acfe9579701f12693dd7a@185.216.75.69:41656,e572ad8a5c190a82c0a68905c76cd7d61d22b578@161.35.39.251:26656,b79965e5cf163ca68d6720f6e9db2c18ea9f5810@72.14.185.165:26656,a5369601c7a7e44a5fdc893540d706c87a48a58c@185.197.251.195:41656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
